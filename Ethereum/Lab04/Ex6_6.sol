//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

// 상속받는 방법 3가지

// constructor 반드시 값을 넣어야반 상속받을 수 있다.
contract Student{
    string public schoolName = "The University of Solidity";
    string public major;
    constructor(string memory _major){
        major = _major;
    }
}

// 방법1 : 바로 넣어버린다.
contract ArtStudent is Student("Art"){}

// 방법2 : 간접적으로 넣기
contract MusicStudent is Student {
    string internal degree = "Music";
    constructor() Student(degree){}
}

contract MathStudent is Student{
    constructor(string memory _major) Student(_major){}
}