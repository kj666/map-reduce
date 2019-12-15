function reduceStat(key, values){

    var a = { sum: values[1], count:1, diff: 0, max: values[1], min: values[1]};
    
    for (var i = 2 ; i < values.length; i++){
        var val = { 
            sum: values[i], 
            count:1, 
            diff: 0,
            max: values[i], 
            min: values[i]};

        var delta = a.sum/a.count - val.sum/val.count; // a.mean - b.mean
        var weight = (a.count * val.count)/(a.count + val.count);
        
        // do the reducing
        a.diff += val.diff + delta*delta*weight;
        a.sum += val.sum;
        a.count += val.count;
        a.min = Math.min(a.min, val.min);
        a.max = Math.max(a.max, val.max);
    }
   
    return a;
}