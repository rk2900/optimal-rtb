camps="1458 2259 2261 2821 2997 3358 3386 3427 3476"
for camp in $camps; do
	bash demo.sh $camp > $camp.log &
done