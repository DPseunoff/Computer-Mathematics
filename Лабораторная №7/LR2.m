clear all
ytt=@(x,y,yt)4*x*yt-(4*x^2-2)*y
y=@(x)(1+x).*exp(x.^2)
y1=1
yt1=1
a=[0,1]
h=0.1

x=a(1):h:a(2);
n=size(x,2);

%метод Эйлера
YE = zeros(1,n);
YE(1) = y1;
YEt = zeros(1,n);
YEt(1) = yt1;
for i = 2:n
   YEt(i) = YEt(i-1) + h*ytt(x(i-1),YE(i-1),YEt(i-1));
   YE(i) = YE(i-1) + h*YEt(i-1);
end

%метод Эйлера c пересчетом
YEP = zeros(1,n);
YEP(1) = y1;
YEPt = zeros(1,n);
YEPt(1) = yt1;
for i = 2:n
   temp = YEPt(i-1) + h*ytt(x(i-1),YEP(i-1),YEPt(i-1));
   YEPt(i) = YEPt(i-1) + h*(ytt(x(i-1),YEP(i-1),YEPt(i-1))+ytt(x(i-1),YEP(i-1),temp))/2;
   YEP(i) = YEP(i-1)+h*(YEPt(i-1)+YEPt(i-1))/2;
end

%метод Рунге-Кутты
YR = zeros(1,n);
YR(1) = y1;
YRt = zeros(1,n);
YRt(1) = yt1;
str=func2str(ytt);
str=str(12:size(str,2));
ytt=str2func(strcat('@(x,y,yt)[yt;(',str,')]'));
for i=2:n
    k1=h*ytt(x(i-1), YR(i-1), YRt(i-1));
    k2=h*ytt(x(i-1)+h/2, YR(i-1)+k1(1)/2, YRt(i-1)+k1(2)/2 );
    k3=h*ytt(x(i-1)+h/2, YR(i-1)+k2(1)/2, YRt(i-1)+k2(2)/2);
    k4=h*ytt(x(i-1)+h, YR(i-1)+k3(1), YRt(i-1)+k3(2));
    dy = (k1+2*k2+2*k3+k4)/6;
    YR(i)=YR(i-1) + dy(1);
    YRt(i)=YRt(i-1) + dy(2);
end 

%метод Адамса
YA = zeros(1,n);
YA(1) = y1;
YAt = zeros(1,n);
YAt(1) = yt1;
for i=2:3
    k1=h*ytt(x(i-1), YA(i-1), YAt(i-1));
    k2=h*ytt(x(i-1)+h/2, YA(i-1)+k1(1)/2, YAt(i-1)+k1(2)/2 );
    k3=h*ytt(x(i-1)+h/2, YA(i-1)+k2(1)/2, YAt(i-1)+k2(2)/2);
    k4=h*ytt(x(i-1)+h, YA(i-1)+k3(1), YAt(i-1)+k3(2));
    dy = (k1+2*k2+2*k3+k4)/6;
    YA(i)=YA(i-1) + dy(1);
    YAt(i)=YAt(i-1) + dy(2);
end 

for i = 4:n
    A1 = 23*ytt(x(i-1),YA(i-1),YAt(i-1));
    A2 = -16*ytt(x(i-2),YA(i-2),YAt(i-2));
    A3 = 5*ytt(x(i-3),YA(i-3),YAt(i-3));
    YAt(i) = YAt(i-1)+h/12*(A1(2)+A2(2)+A3(2));
    YA(i)=YA(i-1)+h/12*(A1(1) +A2(1)+A3(1));
end

hold on
subplot(2,2,1)
plot(x, y(x), x, YE)
title('Метод Эйлера');
xlabel('x')
ylabel('y')
legend('Точное','Приближенное')

subplot(2,2,2)
plot(x, y(x), x, YEP)
title('Метод Эйлера пересчетом');
xlabel('x')
ylabel('y')
legend('Точное','Приближенное')

subplot(2,2,3)
plot(x, y(x), x, YR)
title('Метод Рунге-Кутты');
xlabel('x')
ylabel('y')
legend('Точное','Приближенное')

subplot(2,2,4)
plot(x, y(x), x, YA)
title('Метод Адамса');
xlabel('x')
ylabel('y')
legend('Точное','Приближенное')