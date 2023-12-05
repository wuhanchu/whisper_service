if [ ! -d "./log/" ];then
  mkdir ./log
fi

core_num=${CORE_NUM:-1}
time_out=${TIME_OUT:-600}
param_str=${PARAM_STR}

echo "core_num:$core_num"
echo "time_out:$time_out"
echo "param_str:$param_str"

gunicorn -w $core_num -t $time_out  --worker-connections 2000  --access-logfile - $param_str -b 0.0.0.0:5000 run:app
