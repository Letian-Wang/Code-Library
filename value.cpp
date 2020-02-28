#include <Eigen/Dense>

Eigen::MatrixXd m(row, col);
m(i, j) = d;
//m << d;  Not stable

Eigen::MatrixXd one = MatrixXd::Ones(1,1);

m.array();  // for broadcast

m.block(0,0,1,1);  // start from 0,0, length is 1,1