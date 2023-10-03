//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex6_1{
    event MyFunction(uint result, string name);
    
    function add(uint a, uint b) public{
        uint total = a + b;
        emit MyFunction(total, "add");
    }

    function mul(uint a, uint b) public{
        uint total = a * b;
        emit MyFunction(total, "mul");
    }
}