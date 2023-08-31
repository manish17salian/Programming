// Question: https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true


'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'alternate' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

function alternate(s) {
    const uniqueChars = [...new Set(s)];

    let maxLen = 0;

    for (let i = 0; i < uniqueChars.length; i++) {
        for (let j = i + 1; j < uniqueChars.length; j++) {
            const validChars = [uniqueChars[i], uniqueChars[j]];
            let tempStr = '';
            let valid = true;

            for (const char of s) {
                if (validChars.includes(char)) {
                    if (tempStr[tempStr.length - 1] === char) {
                        valid = false;
                        break;
                    }
                    tempStr += char;
                }
            }

            if (valid) {
                maxLen = Math.max(maxLen, tempStr.length);
            }
        }
    }

    return maxLen;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const l = parseInt(readLine().trim(), 10);

    const s = readLine();

    const result = alternate(s);

    ws.write(result + '\n');

    ws.end();
}
