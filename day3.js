//Recursion
// Print Name N times using recursion

function printName(name, count) {
  if (count <= 0) {
    return;
  }
  console.log(name);
  printName(name, --count);
}

// printName("Ranjeet", 6);

//Print Number 1 to N

function printNumber(N, init = 1) {
  console.log(init);
  if (N === init) return;
  init += 1;
  printNumber(N, init);
}

// printNumber(5);

// Print 1 to N with backtracking

function backtracking(N) {
  if (N < 1) return;
  backtracking(N - 1);
  console.log(N);
}
// backtracking(5);

// print N to 1 with backtracking

function backtracking2(N) {
  console.log(N);
  if (N < 1) return;
  backtracking2(N - 1);
}

backtracking2(6);
