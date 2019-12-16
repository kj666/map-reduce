function mapCPU(){
    emit('CPUUtilization_Average', parseInt(this.CPUUtilization_Average));
}