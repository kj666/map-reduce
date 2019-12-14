function reduceMin(key, values){
    var min = values[0];
    values.forEach(function(val){
        if(val < min) min = val;
    });
    return min;
}