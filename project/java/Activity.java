package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Activity  {

  private String uuid;
  private String title;
  private String description;
  private List<Step> steps;
  private ReviewedControls related-controls;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;

}