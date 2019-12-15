function reduceMedian(key, values){
    if(values.length == 0 ){
        return 0;
    }

    values.sort(function(val1, val2){
        return val1 - val2;
    });

    var middle = Math.floor(values.length/2);

    if(values.length % 2){
        return values[middle];
    }
    return (values[middle -1 ] + values[middle]) / 2.0;
}