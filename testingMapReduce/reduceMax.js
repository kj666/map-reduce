function reduceMax(key, values){
    var max = values[0];
    values.forEach(function(val){
        if(val > max) max = val;
    });
    return max;
}