from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)


def deploy_fund_me():

    account = get_account()
    print(f"account {account} + network {network.show_active()}")
    # pass the price feed address to our fundme contract
    # if we are on a perssitnet network like rinkby, use the associated address
    # otherwise, deploy mocks.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"entrance price - {fund_me.getPrice()}")
    print(f"entrance fee - {fund_me.getEntranceFee()}")
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    pass
    deploy_fund_me()
