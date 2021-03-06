from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIRENMENTS,
)
from web3 import Web3


def deploy_fund_me():
    # account
    account = get_account()
    # if we are on persistent network like rinkeby, use associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRENMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        print(f"The active network is {network.show_active()}")
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me


def main():
    deploy_fund_me()
