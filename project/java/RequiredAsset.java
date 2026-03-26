package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies an asset required to achieve remediation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RequiredAsset  {

  private String uuid;
  private String title;
  private String description;
  private List<SubjectReference> subjects;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}