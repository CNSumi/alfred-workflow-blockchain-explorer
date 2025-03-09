# alfred-workflow-blockchain-explorer

## Command
```sh
bc eth $address # https://etherscan.io/address/$address
bc eth $txid    # https://etherscan.io/tx/$txid

bc sol $token   # https://solscan.io/token/$token
bc sol $txid    # https://solscan.io/tx/$token
bc sol $account # https://solscan.io/account/$account
```

## EVM
- Txid: `^(0x)?[0-9a-fA-F]{64}\\b`
- Address: `^(0x)?[0-9a-fA-F]{40}\\b`

### Chains

| Chain            | Keyword | Explorer                  |
| ---------------- | ------- | ------------------------- |
| Ethereum         | eth     | etherscan.io              |
| Avalance C-Chain | avax    | snowtrace.io              |
| Arbitrum         | arv     | arbiscan.io               |
| Pulse Chain      | pls     | otter.pulsechain.com      |
| BNB Smart Chain  | bsc     | bscscan.io                |
| Matic            | matic   | polygonscan.com           |
| Base             | base    | basescan.org              |
| Fantom           | fantom  | ftmscan.org               |
| Heco             | heco    | hecoinfo.com              |
| Okex             | okex    | oklink.com                |
| Monad Testnet    | monad   | testnet.monadexplorer.com |

## Solana
### Pattern
- Token: `^[0-9a-zA-Z]{43}\\b`
- Address: `^[0-9a-zA-Z]{44}\\b`
- Txid: `^[0-9a-zA-Z]{64}\\b`
### Explorer
- https://solscan.io




# Example:
```sh
bc eth 0xf120007d00480034faf40000e1727c7809734b20
```
