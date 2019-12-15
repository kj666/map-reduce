function finalize(key, value) { 
	value.average = value.sum / value.count;
	value.variance = value.diff / (value.count - 1);
	value.standard_deviation = Math.sqrt(value.variance);
	delete value.diff;
	delete value.sum;
	delete value.count;
	delete value.min;
	delete value.max;
	return value;
}