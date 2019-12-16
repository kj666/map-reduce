function reducePercentile(key, values) {
    const sorted = values.sort(function(a, b) {
        return a - b;
    });
    const pos = (sorted.length - 1) * 0.9;
    const base = Math.floor(pos);
    const rest = pos - base;
    if (sorted[base + 1] !== undefined) {
        return sorted[base] + rest * (sorted[base + 1] - sorted[base]);
    } else {
        return sorted[base];
    }
}