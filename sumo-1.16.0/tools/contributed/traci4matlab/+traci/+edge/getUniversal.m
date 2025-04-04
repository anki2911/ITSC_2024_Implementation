function returnedValue = getUniversal(varID, edgeID)
%getUniversal An internal function to send the get command and read the 
%variable value.

%   Copyright 2019 Universidad Nacional de Colombia,
%   Politecnico Jaime Isaza Cadavid.
%   Authors: Andres Acosta, Jairo Espinosa, Jorge Espinosa.
%   $Id: getUniversal.m 48 2018-12-26 15:35:20Z afacostag $

import traci.constants
global edgeSubscriptionResults

if isempty(edgeSubscriptionResults)
    ReturnValueFunc = traci.RETURN_VALUE_FUNC.edge;
else
    ReturnValueFunc = edgeSubscriptionResults.valueFunc;
end

% Prepare the outgoing message and read the response. The result variable
% is a traci.Storage object
result = traci.sendReadOneStringCmd(constants.CMD_GET_EDGE_VARIABLE,varID,edgeID);
handleReturValueFunc = str2func(ReturnValueFunc(varID));

% Use the proper method to read the variable of interest from the result
returnedValue = handleReturValueFunc(result);