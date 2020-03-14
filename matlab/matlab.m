clear all;


% For loop
for i=1:length(X)
    A(i) = i; 
end

% Concert number to str
str2 = mat2str(j);              

% Slice string
str = [str0,str2,str00,str1,str2,str3];    % Slice string

% Read txt file from first row
X = dlmread(str, '', 1);        

% Create Variable
A = zeros(1,length(X));         

% Contatenate variable
data = cat(1,X,A);              

% Display variable
disp(length(X));               

% Use string name to create variable
name = [str1, str2];
eval( [name, '= data']);        

% save variable to .mat file
file_name = [str0, str2, str00, str1, str2, str4];
save(file_name,variable)            % Save variable to mat file