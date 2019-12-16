function reduceNormalize(key, values){
    
    var norm = [];
    var max = 0;
    var min = 0;
    
    var a = values.toString();
    // Convert string to array
    var b = a.split(',').map(function(item) {
        return parseFloat(item);
    });

    // Get maximum
    b.forEach(function(val){
        if(val > max) max = val;
    });

    // Get minimum
    b.forEach(function(val){
        if(val > max) min = val;
    });
    
    b.forEach(function(value){
        var normalized = (value-min)/(max-min);
        norm.push(normalized);
    });
    //They dont support to export as objects yet
    return norm.toString();
}