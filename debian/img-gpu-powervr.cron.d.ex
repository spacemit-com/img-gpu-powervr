#
# Regular cron jobs for the img-gpu-powervr package.
#
0 4	* * *	root	[ -x /usr/bin/img-gpu-powervr_maintenance ] && /usr/bin/img-gpu-powervr_maintenance
