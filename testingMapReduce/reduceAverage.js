function reduceAverage(key, values){
    var sum = 0;
    var count = 1;
    values.forEach(function(val){
        sum = sum + val;
        count = count +1;
    });
    var avg = (sum /count);
    return avg;
}