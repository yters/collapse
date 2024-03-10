png('images/collapse.png')
ylab = 'Information'
xlab = 'Iteration'
ylim = c(0.05, 0.4)
datacol = 2
dsym = 1
dcol = 'blue'
fsym = 1
fcol = 'red'
degrade <- read.table('results/degrade.txt')
filter <- read.table('results/filter.txt')
plot(degrade[,1],degrade[,datacol],ylim=ylim,ylab=ylab,xlab=xlab,pch=dsym,col=dcol)
par(new=TRUE)
plot(filter[,1],filter[,datacol],ylim=ylim,ylab=ylab,xlab=xlab,pch=fsym,col=fcol)
legend('topright', c('Filtered', 'Regular'), pch=c(fsym, dsym), col=c(fcol, dcol))
title('Filtering Does Not Prevent Model Collapse')
tmp <- dev.off()
