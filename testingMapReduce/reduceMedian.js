function reduceMedian(key, values){

    var median = values[0];
    values.forEach(function(val){
        var middle = Math.floor(values.length/2);

        if(values.length % 2 != 0){
            median = values[middle];
        }
        else{
            median = (values[middle -1 ] + values[middle]) / 2.0;
        }
    });
    return median
}