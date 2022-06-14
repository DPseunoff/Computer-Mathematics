# Тесты
# @(x)(sin(x)).^3 - (cos(x/2)).^2 + 2 [-3;3] 0.2
# @(x) - x.^4 + 3 * x.^3 + 4 * x - 5 [0;2] 0.1
# @(x)sin(x).^3 - 3 * sin(x.^2) + 4 * sin(x) + 4 * x [0;4] 0.2
# @(x)log(10*sin((3 * x./5).^2) + 1) [-3;3] 0.005

clear all;
disp('Введите функцию');
y=input('');
disp('Введите интервал');
interval=input('');
disp('Введите шаг');
step=input('');

#интервал Х
x = interval(1) : step : interval(2);
n = size(x, 2);

#считаем сигмы
sigma1 = 0;
sigma2 = 0;
for i = 1 : n
    if ((i ~= 1) && (i ~= n))
        if (mod(i, 2) == 1)
            sigma2 = sigma2 + y(x(i));
        else
            sigma1 = sigma1 + y(x(i));
        end
    end
end
#считаем интеграл по формуле
I = step / 3 * (y(x(1)) + y(x(n)) + 4*sigma1 + 2*sigma2);
disp(strcat('Примерный результат: ', num2str(I)));