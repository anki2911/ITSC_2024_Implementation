function subscribe(loopID, varargin) 
%subscribe Subscribe to induction loop variable.
%   subscribe(LOOPID) Subscribe to the LAST_STEP_VEHICLE_NUMBER value for
%   the maximum allowed interval.
%   subscribe(LOOPID,VARIDS) Subscribe to the values given in the cell 
%   array of strings VARIDS for the maximum allowed interval.
%   subscribe(...,BEGIN) Subscribe from the time BEGIN to the maximum 
%   allowed end time.
%   subscribe(...,END) Subscribe for the time interval defined by BEGIN and 
%   END.
%   A call to this function clears all previous subscription results.

%   Copyright 2019 Universidad Nacional de Colombia,
%   Politecnico Jaime Isaza Cadavid.
%   Authors: Andres Acosta, Jairo Espinosa, Jorge Espinosa.
%   $Id: subscribe.m 53 2019-01-03 15:18:31Z afacostag $

global loopSubscriptionResults
import traci.constants

% Parse the input
p = inputParser;
p.FunctionName = 'inductionloop.subscribe';
p.addRequired('loopID',@ischar)
p.addOptional('varIDs', {constants.LAST_STEP_VEHICLE_NUMBER}, @iscell)
p.addOptional('subscriptionBegin', constants.INVALID_DOUBLE_VALUE,...
    @(x)(isnumeric(x) && length(x)==1))
p.addOptional('subscriptionEnd', constants.INVALID_DOUBLE_VALUE,...
    @(x)(isnumeric(x) && length(x)==1))
p.parse(loopID, varargin{:})
loopID = p.Results.loopID;
varIDs = p.Results.varIDs;
subscriptionBegin = p.Results.subscriptionBegin;
subscriptionEnd = p.Results.subscriptionEnd;

loopSubscriptionResults = traci.SubscriptionResults(traci.RETURN_VALUE_FUNC.inductionloop);

loopSubscriptionResults.reset()
traci.subscribe(constants.CMD_SUBSCRIBE_INDUCTIONLOOP_VARIABLE,...
    subscriptionBegin, subscriptionEnd, loopID, varIDs)