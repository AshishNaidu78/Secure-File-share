// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileRegistry {
    struct FileMeta {
        string fileHash;
        address uploader;
        uint timestamp;
    }

    mapping(string => FileMeta) public files;

    function registerFile(string memory fileId, string memory hash) public {
        files[fileId] = FileMeta(hash, msg.sender, block.timestamp);
    }

    function getFile(string memory fileId) public view returns (string memory, address, uint) {
        FileMeta memory f = files[fileId];
        return (f.fileHash, f.uploader, f.timestamp);
    }
}
