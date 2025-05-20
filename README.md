
# SPLTokenSolana

Create and Mint an SPL Token on the Solana blockchain using Python.

## Overview

This repository provides a simple Python script to create and mint an SPL (Solana Program Library) token on the Solana blockchain. It demonstrates how to interact with Solana's token program to deploy your own custom token using Python.

## Features

- Create a new SPL token mint
- Create a token account for holding tokens
- Mint tokens to a specified account
- Uses Python and Solana Python SDKs

## Prerequisites

- Python 3.7+
- Solana CLI installed and configured (optional but recommended)
- Access to a Solana RPC endpoint (e.g., https://api.devnet.solana.com for testing)
- A funded Solana wallet keypair (for paying transaction fees and mint authority)

## Installation

1. Clone this repository:

```
git clone https://github.com/Caldegorn/SPLTokenSolana.git
cd SPLTokenSolana
```

2. Create a virtual environment and activate it (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required Python packages:

```
pip install -r requirements.txt
```

*(If `requirements.txt` is not present, install manually:)*

```
pip install solana spl-token
```

## Usage

Edit the `sol.py` script to configure your wallet keypair and RPC endpoint if needed.

Run the script to create and mint your SPL token:

```
python sol.py
```

The script will:

- Connect to the Solana network
- Create a new SPL token mint
- Create a token account for the wallet
- Mint a specified amount of tokens to the token account

## Notes

- This example is mainly for development and testing on Solana Devnet or Testnet.
- Make sure your wallet has enough SOL to pay for transaction fees.
- For mainnet usage, update the RPC endpoint and ensure wallet security.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

