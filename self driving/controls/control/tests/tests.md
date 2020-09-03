## Path Planning
This is only the first mode of testing for the functions. This is not the final test. HIL testing yet to be done

### TO DO

- FIX:- fix the typeerror. Find an alternative for interpolation 
- Find a more intelligent way to design the desired_polyfit.
- desired_polyfit needs fixing
- Update needs fixing along with the model outputs.
- BUG FIX - the weighted average gets into weird issues during interpolation.
- Find a clever way to compute the predicted path.
- speed and model needs to be set.
 
#### FIXED: :heavy_check_mark:
 - figuring out a way to compute predicted in path planning, with model polyfit
 - desired_polyfit and centre_probability consistent with test passing. 
 - Type Error fixed.

## lateral Control
This is also only the first few modes of testing

## FIXED: :heavy_check_mark:
- lookahead distance is fixed.
- curvature is fixed.

## TO DO

- BUG FIX:- is getting into weird issues while computing the steering angle.(higher angle)
- In controller - Integral error needs to be greater than zero. Problems may arise in case of clipping.
- BUG FIX:- In Unwinding
- Check for the override and the lateral fall back condition.