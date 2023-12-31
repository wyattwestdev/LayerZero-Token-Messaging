from eth_abi.packed import encode_packed
from eth_utils import to_bytes
from web3 import Web3

def get_relayer_hex(version: int, value: int) -> str:
    adapterParams = encode_packed(['uint16', 'uint256'], [version, value])
    return Web3.toHex(adapterParams)

def get_lzoracle_config(address: str) -> str:
    return "0x" + address[2:].rjust(64, '0')