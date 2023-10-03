//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

// 계약서1 : Monitor
contract Monitor{
    string public name;

    // 생성자 : 입력 받음
    constructor(string memory _name){
        name = _name;
    }

    function show() public pure returns(string memory){
        return "show";
    }
}

// 게약서 2 : SystemUint
contract SystemUint{
    string public name = "XG12";
    function turnOn() public pure returns(string memory){
        return "turnOn";
    }
}

// 계약서 3 : Computer
contract Computer{
    // 두 계약서를 불러옴
    Monitor public monitor;
    SystemUint public systemUint;

    // 생성자
    constructor(){
        monitor = new Monitor("DW12");
        systemUint = new SystemUint();
    }

    function getAllName() public view returns(string memory, string memory){
        return (monitor.name(), systemUint.name());
    }

    function start() public view returns(string memory, string memory){
        return(monitor.show(), systemUint.turnOn());
    }
}