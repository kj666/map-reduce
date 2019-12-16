function reduceNormalize(key, values){
    var norm = [];
    values.forEach(function(val){
        if(val != NaN){
        var max = 100;
        var min = 0;
      
        var normalized = (val-min)/(max-min);
        norm.push(normalized);
        }
        else{
            norm.push(-1);
        }
    });
    return {norm};
}