Sandbox
=======

Sandbox is the application for learning Genropy framework
(https://github.com/genropy/genropy).  (Currently avaliable only in
italian)

You can try sandbox using **docker**

	docker run -d -p 8080:8080 genropy/sandbox
	
Or you can install it folder genropy_projects 

    git clone https://github.com/genropy/sandbox.git

Genropy webapplications needs a daemon

Run inside another terminal

    gnrdaemon

Now we are ready for running **sandbox** website

    gnrwsgiserve sandbox
    
If you want to edit tutorial files through the application itself run
**gnrwsgiserve** with **remote_edit** option

    gnrwsgiserve sandbox --remote_edit
    

License
=======

The code is licensed under the LGPL license::
    
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.
    
    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.
    
    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
