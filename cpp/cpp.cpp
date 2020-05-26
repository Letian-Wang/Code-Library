(int) round(a)                      // int and round should be used at the same time
use atan2() rather than atan()      // atan2() returns all 4 quadrants, atan() returns 1,4 quadrants
  
#define PI 3.1415926535897932384

// angle operation
  void to_degree(double &angle)
{
    angle = fmod((fmod(angle, 2*PI) + 2*PI), 2*PI);
    angle = angle / PI * 180;
}

bool angle_between(double &target, double &angle1, double &angle2) {
    // In degree. True if between, False if out
    // Which is bigger between the two angle dosen't matter
    // Apply to all range of angles (even larger than 360 of smaller than -360)
    // 1. constarin the angle into [0, 360)
    //    fmod rounded the quotient towards 0
	target = fmod((fmod(target, 360) + 360), 360);
	angle1 = fmod((fmod(angle1, 360) + 360), 360);
	angle2 = fmod((fmod(angle2, 360) + 360), 360);
    // 2. make sure there is a angle range smaller than 180 
    if ((angle2 - angle1) == 0)
        cout << "angle_between: there is no angle range smaller than 180" << endl;
    assert(angle2 - angle1);
    // 3. get the range which is smaller than 180
    double low = min(angle2, angle1); 
    double high = max(angle2, angle1); 
    if (abs(high - low) > 180)
    {
        bool in_0_and_low = (0 <= target && target <= low);
        bool in_high_and_360 = (high <= target && target < 360);
        return in_0_and_low || in_high_and_360;
    }
    else
    {
        return (low <= target && target <= high);                   
    }
}

double round_to_closet_angle(double &target, double &angle1, double &angle2)
{
    // In degree. 
    // Which is bigger between the two angle dosen't matter
    // Apply to all range of angles (even larger than 360 of smaller than -360)
    // 1. constarin the angle into [0, 360)
    //    fmod rounded the quotient towards 0    
	target = fmod((fmod(target, 360) + 360), 360);
	angle1 = fmod((fmod(angle1, 360) + 360), 360);
	angle2 = fmod((fmod(angle2, 360) + 360), 360);
    double high1 = max(target, angle1);
    double low1 = min(target, angle1);
    double high2 = max(target, angle2);
    double low2 = min(target, angle2);
    // remainder rounded the quotient nearstly
    // 2. get the closet distance to each angle
    double distance1 = abs(remainder((high1 - low1), 360));
    double distance2 = abs(remainder((high2 - low2), 360));
    if (distance1 < distance2)  return angle1;
    else    return angle2;
}
double clamp_angle(double &target, double &angle1, double &angle2)
{
    // In degree. 
    // Which is bigger between the two angle dosen't matter
    // Apply to all range of angles (even larger than 360 of smaller than -360)
    if (angle_between(target, angle1, angle2)) return target;
    else return round_to_closet_angle(target, angle1, angle2);
}
