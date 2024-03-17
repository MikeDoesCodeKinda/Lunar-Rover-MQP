function ratedsteps = RateFilter(instructions)
% This function will take a given set of instructions and convert it to
% rounded integer steps that are rated. This means that motors will run at
% roughly the correct rate. For a given time step in the inverse
% kinematics, motors should run a certain amount of steps. In the rated
% instructions, the steps will be based on the ratio of steps in a given
% set of instructions. This will also incorporate remainders and rounding
% since the instructions do not need to be whole numbers. At the end values
% may be rounded since only whole numbers of steps will be run

% Michael Gouveia
% February 20, 2024
% Version 1.0

number_of_lines = length(instructions(:, 1));

steps = instructions(:, 3:end);
step_numbers = instructions(:, 1);
phases = instructions(:, 2);

remainder = zeros(1, 18);
steps_taken = zeros(1, 18);
final_instructions = [];
final_counter = 1;
final_remainder = zeros(1, 18);
final_steps = [];
final_phases = [];
multiplier = zeros(number_of_lines, 1);
for i = 1:number_of_lines
    %disp("i is")
    %disp(i)
    this_phase_instructions = steps(i, :);
    multiplier = 10^6;
    remainder = final_remainder;
    %final_remainder = 0; % testing low multiplier
    for j = 1:18
        if abs(this_phase_instructions(j)) < multiplier && abs(this_phase_instructions(j))~=0
            multiplier = abs(this_phase_instructions(j));
            %multiplier_index = j;
        else
            continue
        end
    end

    if multiplier < 1
        temp_multiplier = 10^6;
        for m = 1:18
            if abs(this_phase_instructions(m)) < 0.5 && i ~= number_of_lines
                this_phase_instructions(m) = 0;
                steps(i+1, m) = steps(i+1, m) + this_phase_instructions(m);
            elseif abs(this_phase_instructions(m)) < 1 && i ~= number_of_lines
                steps(i+1, m) = steps(i+1, m) + this_phase_instructions(m);
                this_phase_instructions(m) = round(this_phase_instructions(m));
            elseif i == number_of_lines && abs(this_phase_instructions(m)) < 1
                this_phase_instructions(m) = round(this_phase_instructions(m));
            end
            if abs(this_phase_instructions(m)) < temp_multiplier && abs(this_phase_instructions(m)) >= 1
                temp_multiplier = this_phase_instructions(m);
            end
        end
        multiplier = temp_multiplier;
    end

    rated_steps = (1/multiplier).*this_phase_instructions;

    rounded_rated_steps = round(rated_steps);

    %remainder = final_remainder;

    for k = 1:round(multiplier)
        final_steps(final_counter) = step_numbers(i);
        final_phases(final_counter) = phases(i);
        final_instructions(final_counter, :) = rounded_rated_steps + round(remainder);
        %ratedsteps(final_counter, :) = [final_steps, final_phases, final_instructions];

        %remainder = remainder + (rounded_rated_steps-rated_steps);
        %remainder = rounded_rated_steps*k - sum(final_instructions(1:final_counter, :));
        %remainder = -rated_steps + final_instructions(final_counter, :);
        %remainder = rated_steps*k - sum(final_instructions,1);
        remainder = rated_steps*k - sum(final_instructions(final_counter-(k-1):final_counter, :), 1);
        steps_taken = steps_taken + final_instructions(final_counter, :);
        final_counter = final_counter + 1;

       

        if k == multiplier
            final_remainder = remainder;
        end
    end
end
%size(final_steps)
%size(final_phases)
%size(final_instructions)
ratedsteps = [final_steps', final_phases', final_instructions];
end







