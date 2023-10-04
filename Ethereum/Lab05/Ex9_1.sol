//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex9_1{
    // 잔액 알아보기
    function getBalanece(address _address) public view returns(uint){
        return _address.balance;
    }

    // payable > 모디파이어 역할. 버튼이 빨간색임.
    function getMsgValue() public payable returns(uint){
        return msg.value;
    }
}