//factorial
function factorial(n) {
    if (n == 0) {
        return 1
    }
    return n * factorial(n - 1);
}

console.log(factorial(3));

//reverse an arr ay

function revArray(array, start, end) {

    if (start >= end) {
        console.log(array)
        return array;
    }
    const tempArr = array[start];
    array[start] = array[end];
    array[end] = tempArr;

    revArray(array, start + 1, end - 1);

}



revArray([1, 2, 3, 4, 5, 6], 0, 5);


//check for palindrome

function checkPalindrome(counter, string) {
    if (counter >= string.length / 2) return true;
    if (string[counter] !== string[string.length - counter - 1]) return false;
    return checkPalindrome(counter + 1, string);
}

console.log(checkPalindrome(0, "madam"))