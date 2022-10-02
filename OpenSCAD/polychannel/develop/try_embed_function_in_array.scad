function test_func() = [5, 5, 5];
function test_func2() = [[6, 6, 6], [7, 7, 7]];

temp_test_func2 = test_func2();
list_of_vectors = [
    [0, 0, 0],
    [1, 1, 1],
    test_func(),
    each test_func2(),
    [8, 8, 8],
    each temp_test_func2,
    [9, 9, 9],
    each temp_test_func2
];

echo(list_of_vectors);
echo(test_func2());
