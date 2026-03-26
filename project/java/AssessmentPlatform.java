package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Used to represent the toolset used to perform aspects of the assessment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPlatform  {

  private String uuid;
  private String title;
  private List<UsesComponent> uses-components;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}