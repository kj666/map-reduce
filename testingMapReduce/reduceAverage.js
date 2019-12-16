function reduceAverage(key, values){
    var sum = 0;
    var count = 1;
    var a = values.toString();
    // Convert string to array
    var b = a.split(',').map(function(item) {
        return parseFloat(item);
    });
    b.forEach(function(val){
        sum = sum + val;
        count = count +1;
    });
    var avg = (sum /count);
    return avg;
}