from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import contract_address, abi


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract_address)

#0x52AE1eeb80cf2EA2B78C7D4fF6010C6984629Fb2
#0x64890774E26350A7639c3C78926eBfC89B6E4D04
#0x92be4c3f2AE40C162E5F61572b78fB28fb0381C3
#0xF828541b717B163eb9E6C6B5370b1bd5a07E69AE 
#0x2884e48075c39540d4DaC07c80a85D2ce6D0fA78

#geth --datadir data --networkid 150220241016 --unlock 0x52AE1eeb80cf2EA2B78C7D4fF6010C6984629Fb2 --allow-insecure-unlock --http --http.corsdomain="*" --http.api web3,eth,debug,personal,net,miner --miner.etherbase 0x52AE1eeb80cf2EA2B78C7D4fF6010C6984629Fb2

print(w3.eth.get_balance("0x52AE1eeb80cf2EA2B78C7D4fF6010C6984629Fb2"))
print(w3.eth.get_balance("0x64890774E26350A7639c3C78926eBfC89B6E4D04"))
print(w3.eth.get_balance("0x92be4c3f2AE40C162E5F61572b78fB28fb0381C3"))
print(w3.eth.get_balance("0xF828541b717B163eb9E6C6B5370b1bd5a07E69AE"))
print(w3.eth.get_balance("0x2884e48075c39540d4DaC07c80a85D2ce6D0fA78"))