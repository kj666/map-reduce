function reduceStat(key, values){

    var a = values.toString();
    // Convert string to array
    var b = a.split(',').map(function(item) {
        return parseFloat(item);
    });

    var a = { sum: b[1], count:1, diff: 0, max: b[1], min: b[1]};
    
    for (var i = 2 ; i < b.length; i++){
        var val = { 
            sum: b[i], 
            count:1, 
            diff: 0,
            max: b[i], 
            min: b[i]};

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