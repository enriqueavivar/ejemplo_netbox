from extras.scripts import Script, StringVar, ChoiceVar
from dcim.models import Site
import yaml

class SiteStatusReport(Script):
    class Meta:
        name = "Site Status Report"
        description = "Lists sites filtered by status and outputs them in YAML format."

    # Filter option
    status_filter = ChoiceVar(
        choices=[
            ('active', 'Active'),
            ('planned', 'Planned')
        ],
        required=True,
        label="Site Status Filter"
    )

    def run(self, data, commit):
        status = data['status_filter']

        # Get matching sites
        sites = Site.objects.filter(status=status)

        results = []

        for site in sites:
            # Log line
            log_line = f"#{site.id}: {site.name} - {site.get_status_display()}"
            self.log_info(log_line)

            # Append site data for YAML output
            results.append({
                'id': site.id,
                'name': site.name,
                'status': site.get_status_display()
            })

        # Output YAML
        output_yaml = yaml.dump(results, sort_keys=False)
        return output_yaml
