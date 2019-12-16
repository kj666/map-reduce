function reduceMedian(key, values){

    var median = values[0];
    var a = values.toString();
    // Convert string to array
    var b = a.split(',').map(function(item) {
        return parseFloat(item);
    });
    b.forEach(function(val){
        var middle = Math.floor(values.length/2);

        if(b.length % 2 != 0){
            median = values[middle];
        }
        else{
            median = (b[middle -1 ] + b[middle]) / 2.0;
        }
    });
    return median
}