Feature: Login

	@login
	Scenario: Login valid
		Given Preparing valid data admin
		When Logging in
		Then Session created