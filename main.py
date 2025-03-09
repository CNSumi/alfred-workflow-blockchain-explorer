# -*- coding: utf-8 -*-
import re
import sys
import webbrowser

evm_pattern = {"address": "0x[0-9a-fA-F]{40}\\b", "tx": "0x[0-9a-fA-F]{64}\\b"}
sol_pattern = {
    "token": "^[0-9a-zA-Z]{43}\\b",
    "addr": "^[0-9a-zA-Z]{44}\\b",
    "tx": "^[0-9a-zA-Z]{64}\\b",
}


class Chain:
    def __init__(
        self,
        name,
        explorer,
        pattern={},
    ):
        self.name = name
        self.explorer = explorer
        self.pattern = pattern


class Navigator:
    def __init__(self):
        self.chains = {}

    def register(self, chain):
        self.chains[chain.name.lower()] = chain

    def process(self, query):
        fields = re.split(r"\s+", query.strip())
        if len(fields) < 2:
            return

        network = fields[0].lower()
        query = fields[1]

        if network in self.chains:
            for name, pattern in self.chains[network].pattern.items():
                if re.match(pattern, query):
                    url = f"https://{self.chains[network].explorer}/{name}/{query}"
                    print(f"navigate to: {url}")
                    webbrowser.open_new_tab(url)
                    return


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        navigator = Navigator()
        navigator.register(Chain("eth", "etherscan.io", evm_pattern))
        navigator.register(Chain("avax", "snowtrace.io", evm_pattern))
        navigator.register(Chain("arb", "arbiscan.io", evm_pattern))
        navigator.register(Chain("pls", "otter.pulsechain.com", evm_pattern))
        navigator.register(Chain("bsc", "bscscan.com", evm_pattern))
        navigator.register(Chain("matic", "polygonscan.com", evm_pattern))
        navigator.register(Chain("base", "basescan.org", evm_pattern))
        navigator.register(Chain("fantom", "ftmscan.com", evm_pattern))
        navigator.register(Chain("heco", "hecoinfo.com", evm_pattern))
        navigator.register(Chain("okex", "oklink.com", evm_pattern))
        navigator.register(Chain("monad", "testnet.monadexplorer.com", evm_pattern))
        navigator.register(Chain("sol", "solscan.io", sol_pattern))

        navigator.process(sys.argv[1])
