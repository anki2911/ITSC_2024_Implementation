function setApparentDecel(typeID, apparentDecel)
%setApparentDecel Sets the apparent deceleration in m/s^2.
%   setApparentDecel(TYPEID,APPARENTDECEL) Sets the apparent deceleration
%   in m/s^2 of vehicles of this type.

%   Copyright 2019 Universidad Nacional de Colombia,
%   Politecnico Jaime Isaza Cadavid.
%   Authors: Andres Acosta, Jairo Espinosa, Jorge Espinosa.
%   $Id: setApparentDecel.m 54 2019-01-03 15:41:54Z afacostag $

import traci.constants
traci.sendDoubleCmd(constants.CMD_SET_VEHICLETYPE_VARIABLE,...
    constants.VAR_APPARENT_DECEL, typeID, apparentDecel);