function reduceNormalize(key, values){
    
    var max = 0;
    var min = 0;
    values.forEach(function(val){
        if(val > max) max = val;
    });

    values.forEach(function(val){
        if(val > max) min = val;
    });

    var norm = [];

    values.forEach(function(val){
        if(val != NaN){
        
        var normalized = (val-min)/(max-min);
        norm.push(normalized);
        }
        else{
            norm.push(-1);
        }
    });
    return {norm};
}