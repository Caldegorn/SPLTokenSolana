from solana.rpc.api import Client
from solana.keypair import Keypair
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID

client = Client("https://api.mainnet-beta.solana.com")
payer = Keypair()  # Your wallet keypair

# Create new token mint
token = Token.create_mint(
    client,
    payer,
    payer.public_key,
    None,  # Freeze authority
    9,  # Decimals
    TOKEN_PROGRAM_ID,
)

# Create token account for the payer
token_account = token.create_account(payer.public_key)

# Mint tokens to the token account
token.mint_to(token_account, payer.public_key, 1000000000)  # Mint 1 token with 9 decimals
