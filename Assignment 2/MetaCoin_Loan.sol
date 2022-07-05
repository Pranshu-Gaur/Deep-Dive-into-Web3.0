// SPDX-License-Identifier: MIT
pragma solidity >=0.4.25 <0.7.0;

contract MetaCoin {
	mapping (address => uint256) balances;

	event Transfer(address indexed _from, address indexed _to, uint256 _value);

	constructor() public {
		balances[tx.origin] = 100000;
	}

	function sendCoin(address receiver, uint256 amount, address sender) public returns(bool sufficient) {
		if (balances[sender] < amount) return false;
		balances[sender] -= amount;
		balances[receiver] += amount;
		emit Transfer(sender, receiver, amount);
		return true;
	}


	function getBalance(address addr) public view returns(uint256) {
		return balances[addr];
	}
}

contract Loan is MetaCoin {

    mapping (address => uint256) private loans;
     
    event Request(address indexed _from, uint256 P, uint R, uint T, uint256 amt);
    
    address private Owner;

    
    modifier isOwner() {
        require(msg.sender==Owner,"You are not the Owner");
        _;
    }
    
    constructor() public {
        Owner = msg.sender;
    }
    
    function mulDiv (uint256 x, uint256 y, uint256 z) internal pure returns (uint256)
    {
        uint256 a = x / z; uint256 b = x % z; // x = a * z + b
        uint256 c = y / z; uint256 d = y % z; // y = c * z + d
        return a * c * z + a * d + b * c + b * d / z;
    }
    function getCompoundInterest(uint256 principle, uint rate, uint time) public pure returns(uint256) {
        
        uint256 P=principle*1e18; uint256 R = rate; uint256 T=time;
        while(T!=0){
            P += mulDiv(P, R, 100);
            T -= 1;
        }
        uint256 z = P/1e17;
        P/=1e18;
        if((z-P*10)>=5){
            P++; // To check if P should be rounded off to the next integer;
        }
        return P;
    }
    
    function reqLoan(uint256 principle, uint rate, uint time) public returns(bool correct) {
        uint256 toPay = getCompoundInterest(principle, rate, time);
        if(msg.sender == Owner) return false;
        if(toPay>=principle){
            loans[msg.sender]+=toPay;
            emit Request(msg.sender,principle,rate,time,toPay);
            return true;
        }
        return false;
    }
    
    function getOwnerBalance() public view returns(uint256) {
        return getBalance(Owner);
	}

    function settleDues(address to_settle) isOwner public returns (bool) {
        if(sendCoin(to_settle,loans[to_settle],Owner)){
            loans[to_settle]=0;
            return true;
        }
        return false;
    }
    function viewDues(address account) isOwner public view returns (uint256){
        return loans[account];
    }
}
